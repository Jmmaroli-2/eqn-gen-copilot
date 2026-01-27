# HTML Report Generator for equation estimation results
# Author: John M. Maroli

import os
import sys
import io
import base64
from datetime import datetime
from contextlib import contextmanager

class HTMLReportGenerator:
    """
    Captures terminal output and generates an HTML report with embedded plots.
    """
    
    def __init__(self):
        self.captured_output = []
        self.original_stdout = None
        self.original_stderr = None
        
    @contextmanager
    def capture_output(self):
        """Context manager to capture stdout and stderr"""
        # Create a StringIO object to capture output
        captured_stdout = io.StringIO()
        captured_stderr = io.StringIO()
        
        # Save original streams
        self.original_stdout = sys.stdout
        self.original_stderr = sys.stderr
        
        # Create a tee that writes to both original and captured
        class TeeStream:
            def __init__(self, original, captured):
                self.original = original
                self.captured = captured
                
            def write(self, text):
                self.original.write(text)
                self.original.flush()
                self.captured.write(text)
                
            def flush(self):
                self.original.flush()
                self.captured.flush()
            
            def fileno(self):
                """Return the file descriptor of the original stream"""
                try:
                    return self.original.fileno()
                except (AttributeError, io.UnsupportedOperation):
                    return -1
            
            def isatty(self):
                """Check if the original stream is a TTY"""
                try:
                    return self.original.isatty()
                except (AttributeError, io.UnsupportedOperation):
                    return False
        
        try:
            # Replace stdout and stderr
            sys.stdout = TeeStream(self.original_stdout, captured_stdout)
            sys.stderr = TeeStream(self.original_stderr, captured_stderr)
            
            yield
            
        finally:
            # Restore original streams
            sys.stdout = self.original_stdout
            sys.stderr = self.original_stderr
            
            # Store captured output
            stdout_value = captured_stdout.getvalue()
            stderr_value = captured_stderr.getvalue()
            
            if stdout_value:
                self.captured_output.append(stdout_value)
            if stderr_value:
                self.captured_output.append(stderr_value)
    
    def get_captured_text(self):
        """Get all captured output as a single string"""
        return ''.join(self.captured_output)
    
    def generate_html_report(self, output_dir='./output', report_name='report.html'):
        """
        Generate an HTML report with captured output and embedded plots.
        
        Args:
            output_dir: Directory where plots are saved and where report will be saved
            report_name: Name of the HTML report file
        """
        # Get captured text
        terminal_output = self.get_captured_text()
        
        # Find all plot files in output directories
        plot_files = []
        if os.path.exists(output_dir):
            for root, dirs, files in os.walk(output_dir):
                for file in files:
                    if file.endswith('.pdf') or file.endswith('.png') or file.endswith('.jpg'):
                        plot_files.append(os.path.join(root, file))
        
        # Generate HTML content
        html_content = self._generate_html_template(terminal_output, plot_files, output_dir)
        
        # Save HTML report
        report_path = os.path.join(output_dir, report_name)
        os.makedirs(output_dir, exist_ok=True)
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"\nHTML report saved to: {report_path}")
        return report_path
    
    def _generate_html_template(self, terminal_output, plot_files, output_dir):
        """Generate the HTML template with styling and content"""
        
        # Convert PDF plots to images or provide links
        plot_html = ""
        if plot_files:
            plot_html = "<h2>Generated Plots</h2>\n"
            for plot_file in sorted(plot_files):
                rel_path = os.path.relpath(plot_file, output_dir)
                file_name = os.path.basename(plot_file)
                
                # For PDFs, provide a link
                if plot_file.endswith('.pdf'):
                    plot_html += f'''
                    <div class="plot-container">
                        <h3>{file_name}</h3>
                        <p><a href="{rel_path}" target="_blank">View PDF Plot: {file_name}</a></p>
                    </div>
                    '''
                else:
                    # For images, embed them
                    try:
                        with open(plot_file, 'rb') as f:
                            img_data = base64.b64encode(f.read()).decode('utf-8')
                            plot_html += f'''
                            <div class="plot-container">
                                <h3>{file_name}</h3>
                                <img src="data:image/png;base64,{img_data}" alt="{file_name}" />
                            </div>
                            '''
                    except Exception as e:
                        plot_html += f'''
                        <div class="plot-container">
                            <h3>{file_name}</h3>
                            <p>Error loading image: {str(e)}</p>
                        </div>
                        '''
        
        # Generate timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Build HTML document
        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Equation Estimation Report</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        
        .header h1 {{
            margin: 0 0 10px 0;
            font-size: 2.5em;
        }}
        
        .timestamp {{
            font-size: 0.9em;
            opacity: 0.9;
        }}
        
        .section {{
            background: white;
            padding: 25px;
            margin-bottom: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        
        h2 {{
            color: #667eea;
            border-bottom: 2px solid #667eea;
            padding-bottom: 10px;
            margin-top: 0;
        }}
        
        .terminal-output {{
            background-color: #1e1e1e;
            color: #d4d4d4;
            padding: 20px;
            border-radius: 5px;
            overflow-x: auto;
            font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
            font-size: 13px;
            line-height: 1.5;
            white-space: pre-wrap;
            word-wrap: break-word;
        }}
        
        .plot-container {{
            margin: 20px 0;
            padding: 15px;
            background: #f9f9f9;
            border-radius: 5px;
            border: 1px solid #e0e0e0;
        }}
        
        .plot-container h3 {{
            margin-top: 0;
            color: #555;
            font-size: 1.1em;
        }}
        
        .plot-container img {{
            max-width: 100%;
            height: auto;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        
        .plot-container a {{
            color: #667eea;
            text-decoration: none;
            font-weight: 500;
        }}
        
        .plot-container a:hover {{
            text-decoration: underline;
        }}
        
        .footer {{
            text-align: center;
            margin-top: 40px;
            padding: 20px;
            color: #666;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Equation Estimation Report</h1>
        <p class="timestamp">Generated on: {timestamp}</p>
    </div>
    
    <div class="section">
        <h2>Terminal Output</h2>
        <div class="terminal-output">{self._escape_html(terminal_output)}</div>
    </div>
    
    {plot_html if plot_html else ""}
    
    <div class="footer">
        <p>Generated by eqn-gen framework</p>
    </div>
</body>
</html>
'''
        return html
    
    def _escape_html(self, text):
        """Escape HTML special characters"""
        return (text
                .replace('&', '&amp;')
                .replace('<', '&lt;')
                .replace('>', '&gt;')
                .replace('"', '&quot;')
                .replace("'", '&#39;'))

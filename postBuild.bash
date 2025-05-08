#!/bin/bash

# expose jupyter's javascript object in the frontend
mkdir -p ~/.jupyter
cat > ~/.jupyter/jupyter_server_config.py <<EOF
c = get_config()  #noqa
c.LabApp.expose_app_in_browser = True
EOF

# configure the application launcher
mkdir -p ~/.local/share/jupyter/jupyter_app_launcher
cat > ~/.local/share/jupyter/jupyter_app_launcher/jp_app_launcher.yaml <<EOF
- title: Visual Search and Summarization
  description: Learn to implement VSS at your company.
  icon: /project/.workshop/_static/nvidia-icon.svg
  source: http://localhost:\$PORT/
  cwd: "/project/.workshop"
  args:
    - "python3"
    - "-m"
    - "http.server"
    - "\$PORT"
  type: local-server
  catalog: NVIDIA DevX Workshop
EOF
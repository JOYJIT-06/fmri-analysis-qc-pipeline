import os
import yaml

class Config:
    def __init__(self, project_root):
        self.project_root = project_root
        self.config_path = os.path.join(project_root, 'configs/analysis_params.yaml')
        with open(self.config_path, 'r') as f:
            self.params = yaml.safe_load(f)

    def get(self, section, key):
        return self.params.get(section, {}).get(key, None)
import os
import yaml
from box import Box
import logging.config

package_path = os.path.dirname(os.path.abspath(__file__))

# loading base config
trn_config_path = os.path.join(package_path, "configs", "train_rf.yml")
with open(trn_config_path, "r") as ymlfile:
    cfg = Box(yaml.safe_load(ymlfile))

# loading logger config
log_path = os.path.join(package_path, cfg.base.path.logs)
log_config_path = os.path.join(
    package_path, 'configs', cfg.base.path.log_config)


os.makedirs(log_path, exist_ok=True)
if os.path.exists(log_config_path):
    with open(log_config_path, "r") as ymlfile:
        log_config = yaml.safe_load(ymlfile)

    # Set up the logger configuration
    logging.config.dictConfig(log_config)
else:
    raise FileNotFoundError(
        f"Log yaml configuration file not found in {cfg.base.path.log_config}")

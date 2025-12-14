from networksecurity.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from networksecurity.entity.config_entity import DataValidationConfig
from networksecurity.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import os
from scipy.stats import ks_2samp
import pandas as pd
import sys
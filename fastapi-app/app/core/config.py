import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


class Settings:
	def __init__(self) -> None:
		self.base_dir = Path(__file__).resolve().parents[2]
		self.service_name = os.getenv("SERVICE_NAME", "ai-service")

		configured_output_dir = os.getenv("OUTPUT_DIR", "storage/output")
		self.output_dir = (self.base_dir / configured_output_dir).resolve()


settings = Settings()


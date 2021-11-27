
import sys
sys.path.append("pixray")
import clipit
# To reset settings to default
pixray.reset_settings()
# You can use "|" to separate multiple prompts
prompts = "underwater city"
# You can trade off speed for quality: draft, normal, better, best
quality = "normal"
# Aspect ratio: widescreen, square
aspect = "widescreen"
# Add settings
pixray.add_settings(prompts=prompts, quality=quality, aspect=aspect)
# Apply these settings and run
settings = pixray.apply_settings()
pixray.do_init(settings)
pixray.do_run(settings)

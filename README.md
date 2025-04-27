# software_testing_hw3

Mutators used for the comment_validator were cosmic-ray
install it with 'pip install cosmic'

set up cosmic-ray.toml with this command:

echo "[cosmic-ray]
module-path = [\"comment_validator.py\"]
test-command = "python -m unittest discover"
timeout = 30

[cosmic-ray.distributor]
name = \"local\"" > cosmic-ray.toml

then ran the following commands: 

cosmic-ray init cosmic-ray.toml session.json\n
cosmic-ray exec cosmic-ray.toml session.json\n
cr-report session.json > report.txt\n
cat report.txt

# OmnilyticsAssignment

This program is the solution of following Omnilytics Assignment

Assignment Link: https://docs.google.com/document/d/1mNl2PJ4CxEq9qQCZV0VZDbPCj5ODPqaLvq2Zonw9dfk/edit#heading=h.gjdgxs

# Solution Step by Step

# Download / Copy OmnilyticsAssignment program in home directory

# Get into OmnilyticsAssignment working directory
cd ~/OmnilyticsAssignment

# Execute Challenge A program
python ChallengeAGenerateData.py

# Check Challenge A program output in host
less challenge_a_output.txt

# Execute Challenge B program
python ChallengeBProcessData.py

# Check Challenge B program output in host
less challenge_b_output.txt

# For Challenge C, creating shared volume between host and docker_container if not exists
mkdir ~/OmnilyticsAssignment/shared_volume

# Copy Challenge B python program code and Challenge A program output into shared volume directory
cp ChallengeBProcessData.py shared_volume/

cp challenge_a_output.txt shared_volume/

# Remove previous docker image if exists
docker rmi -f omnilytics_image

# Create/build docker image
docker build -t omnilytics_image .

# Remove previous docker container if exists
docker rm -f omnilytics_container

# Run docker container
docker run --name omnilytics_container -v ~/OmnilyticsAssignment/shared_volume:/usr/src/app -d omnilytics_image

# Check omnilytics_container container
docker ps -a

# Check log of omnilytics_container container
docker logs <container_id>

# Check Challenge B program output in host
less shared_volume/challenge_b_output.txt


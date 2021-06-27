# Download / Copy OmnilyticsAssignment program in home directory

# Get into OmnilyticsAssignment working directory
cd ~/OmnilyticsAssignment

# Execute Challenge A program
python ChallengeAGenerateData.py

# Creating shared volume between host and docker_container if exists
mkdir ~/OmnilyticsAssignment/shared_volume

# Copy Challenge B python program code and Challenge A program output into shared volume directory
cp ChallengeBProcessData.py shared_volume/
cp challenge_a_output.txt shared_volume/

# Remove previous docker image if exists
docker rmi -f omnilytics_image

# Create/build docker image
docker build -t omnilytics_image .

# Remove previous docker container if exists :
docker rm -f omnilytics_container

# Run docker container
docker run --name omnilytics_container -v ~/OmnilyticsAssignment/shared_volume:/usr/src/app -d omnilytics_image

# Check omnilytics_container container
docker ps -a

# Check log of omnilytics_container container
docker logs <container_id>

# Check Challenge B program output in host
less shared_volume/challenge_b_output.txt

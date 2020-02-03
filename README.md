# GCP_CI-CD
my GCP CI/DI project
In this project, 2 functions are built. 
1.	@ root pathThe first function will visualize the most up to date coronavirus distribution. this function will first web scrape website to get the data with BeautifulSoup and then visualize the data.
2.	@ /upload path The second function is designed to let the user upload a ‘.jpg’ file and transfer it to a greyscale picture.


To run the project:

Manual deploy:

	make all

GCP Cloud Build:

	Connect the GCP Cloud Build to this git repository and trigger the build.

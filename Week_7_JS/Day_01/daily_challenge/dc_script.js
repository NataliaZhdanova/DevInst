// Instructions
// In this exercise, you will use object oriented programming concepts to define and use a custom object in JavaScript.

// Create a class named Video. The class should be constructed with the following parameters:
// title (a string)
// uploader (a string, the person who uploaded it)
// time (a number, the duration of the video - in seconds)
// Create a method called watch() which displays a string as follows:
// “uploader parameter watched all time parameter of title parameter!”
// Instantiate a new Video instance and call the watch() method.
// Instantiate a second Video instance with different values.


class Video {
	constructor(title, uploader, time) {
		this.title = title;
		this.uploader = uploader;
        this.time = time;
	}
	watch() {
		console.log(`${this.uploader} watched all ${this.time} seconds of the "${this.title}" video!`);
	}
}

const video1 = new Video("War and Peace", "John Doe", 90);
video1.watch();
const video2 = new Video("Fear and Pride", "Jane Dow", 120);
video2.watch();

// Bonus: Use an array to store data for five Video instances (ie. title, uploader, time)
// Think of the best data structure to save this information within the array.
// Bonus: Loop through the array to instantiate those instances.

const arrVideos = [
    {title: "Misterious Cat", uploader: "Koleen Wolf", time: 60},
    {title: "A True Trooper", uploader: "Jamie Smith", time: 180},
    {title: "A Day in May", uploader: "Norco Leery", time: 120},
    {title: "The School is for Cool", uploader: "Tom Trend", time: 90},
    {title: "A Brick in the Wall", uploader: "Rocky Horror", time: 240}
];

const videoInstances = arrVideos.map(video => new Video(video.title, video.uploader, video.time));
videoInstances.forEach(video => video.watch());
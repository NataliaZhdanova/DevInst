// In a separate Javascript file, named Exercise3.js, create a new Class Component called Exercise that contains some HTML tags.
// create a <h1> tag and set its color to red, and the background color to lightblue.
// create a paragraph, a link, a form, an image and a list.
// Import Exercise component to the App.js file and display it.

// Add the below object to the component Exercise. Use this object to style the <h1>.
import "./Exercise.css";

const style_header = {
  color: "white",
  backgroundColor: "DodgerBlue",
  padding: "10px",
  fontFamily: "Arial"
};

// <h1 style={{color:"red", backgroundColor:"lightblue"}} >Some header</h1>

function Exercise() {
    return (
        <div>
          <h1 style={style_header} >Some header</h1>
          <p class="para">Some paragraph</p>
          <a href={{URL}}>Some link</a>
          <form>
            <input></input>
            <button>Submit</button>
          </form>
          <img src={{URL}} alt=""></img>
          <ul>
            <li>Some list item</li>
            <li>Some list item</li>
          </ul>

        </div>
      );
  }

  export default Exercise;
import React from "react";

const Form = ({ formData, handleChange }) => {
  return (
    <div>
      <form method="get" action="/">
        <label>
          First Name:
          <input type="text" name="firstName" value={formData.firstName} onChange={handleChange} />
        </label>
        <br />
        <label>
          Last Name:
          <input type="text" name="lastName" value={formData.lastName} onChange={handleChange} />
        </label>
        <br />
        <label>
          Age:
          <input type="text" name="age" value={formData.age} onChange={handleChange} />
        </label>
        <br />
        <label>
          Gender:
          <input type="radio" name="gender" value="male" checked={formData.gender === "male"} onChange={handleChange} /> Male
          <input type="radio" name="gender" value="female" checked={formData.gender === "female"} onChange={handleChange} /> Female
        </label>
        <br />
        <label>
          Destination:
          <select name="destination" value={formData.destination} onChange={handleChange}>
            <option value="Japan">Japan</option>
            <option value="USA">USA</option>
            <option value="Europe">Europe</option>
          </select>
        </label>
        <br />
        <label>
          Lactose-free:
          <input type="checkbox" name="lactoseFree" checked={formData.lactoseFree} onChange={handleChange} />
        </label>
        <br />
        <label>
          Nuts-free:
          <input type="checkbox" name="nutsFree" checked={formData.nutsFree} onChange={handleChange} />
        </label>
        <br />
        <label>
          Vegan:
          <input type="checkbox" name="vegan" checked={formData.vegan} onChange={handleChange} />
        </label>
        <br />
        <button type="submit">Submit</button>
      </form>

      <div>
        <h2>Entered Data:</h2>
          <p>First Name: {formData.firstName}</p>
          <p>Last Name: {formData.lastName}</p>
          <p>Age: {formData.age}</p>
          <p>Gender: {formData.gender}</p>
          <p>Destination: {formData.destination}</p>
          <p>Lactose-free: {formData.lactoseFree ? "Yes" : "No"}</p>
          <p>Nuts-free: {formData.nutsFree ? "Yes" : "No"}</p>
          <p>Vegan: {formData.vegan ? "Yes" : "No"}</p>
        </div>
    </div>

  );
};

export default Form;

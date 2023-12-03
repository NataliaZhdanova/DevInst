import { useState } from "react";
import Form from "./Form";

const App = () => {
  const [formData, setFormData] = useState({
    firstName: "",
    lastName: "",
    age: "",
    gender: "",
    destination: "",
    lactoseFree: false,
    nutsFree: false,
    vegan: false
  });

  const handleChange = (event) => {
    const { name, value, type, checked } = event.target;
    const updatedValue = type === "checkbox" ? checked : value;

    setFormData((prevData) => ({
      ...prevData,
      [name]: updatedValue,
    }));
  };

  return (
    <div>
      <h1>Form Processing</h1>
      <Form formData={formData} handleChange={handleChange} />
    </div>
  );
};

export default App;

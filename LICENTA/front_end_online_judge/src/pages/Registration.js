import React, { useState } from "react";
import "../index.css";
import "../style.css";
import { Link } from "react-router-dom";
import httpClient from "./httpClient";

const Registration = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const User_Registration = async () => {
    console.log(username, password);

    try {
      const resp = await httpClient.post("//localhost:5000/register", {
        username,
        password,
      });
      window.location.href = "/";
    } catch (error) {
      if (error.response.status === 401) {
        alert("invalied Credential");
      }
    }
  };

  return (
    <div>
      <Link to="/" className="btn btn-light my-3 mx-5">
        Go Back
      </Link>
      <h3 className="center">Registration</h3>
      {/* Registration form */}

      <div className="container">
        <div className="forms">
          <div className="form signup">
            <span className="title">Registration</span>
            <form action="#">
             
              <div className="input-field">
                <input
                  type="text"
                  placeholder="Enter your username"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  required
                />
              </div>
              <div className="input-field">
                <input
                  type="password"
                  className="password"
                  placeholder="Create a password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  required
                />
              </div>
              
              
              <div className="input-field button">
                <input
                  type="button"
                  defaultValue="Register Now"
                  onClick={() => User_Registration()}
                />
              </div>
            </form>
            
          </div>
        </div>
      </div>

      {/* Registration form */}
    </div>
  );
};

export default Registration;

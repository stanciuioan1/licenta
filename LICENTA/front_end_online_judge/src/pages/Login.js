import React, { useState } from "react";
import "../index.css";
import { Link } from "react-router-dom";
import httpClient from "./httpClient";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const LogInUser = async () => {
    console.log(username, password);

    try {
      const resp = await httpClient.post("//localhost:5000/login", {
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
      <h3 className="center">Log Into Your Account</h3>
      {/* login form */}

      <div className="container">
        <div className="forms">
          <div className="form login">
            <span className="title">Login</span>
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
                  placeholder="Enter your password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  required
                />
              </div>
              
              <div className="input-field button">
                <input
                  type="button"
                  defaultValue="Login Now"
                  onClick={() => LogInUser()}
                />
              </div>
            </form>
            <div className="login-signup">
              <span className="text1">
                Not a member?
                <a href="/register" className="text1 signup-link">
                  Signup now
                </a>
              </span>
            </div>
          </div>
        </div>
      </div>

      {/* login form */}
    </div>
  );
};

export default Login;

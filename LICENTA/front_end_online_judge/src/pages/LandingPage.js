import React, { useState, useEffect } from "react";
import "../index.css";
import { Container, Row, Col, Button } from "react-bootstrap";
import httpClient from "./httpClient";
import { User } from "../types";


const LandingPage = () => {
  const [loading, setLoading] = useState(true);
  const [loggedIn, setLoggedIn] = useState(false);
  const [user, setUser] = useState(User);
  const logoutUser = async () => {
    await httpClient.post("//localhost:5000/logout");
    window.location.href = "/";
  };

  
  const numbers = [1, 2, 3, 4, 5];
  const listItems = numbers.map((number) =>
  <h1 ><a href={`/problem?no=${number.toString()}`}>
    {number}
  </a></h1>
);

  useEffect(() => {
    (async () => {
      try {
        const resp = await httpClient.get("//localhost:5000/user");

        console.log(resp.data)

        setUser(resp.data);
        setLoading(false);
        setLoggedIn(true);

      } catch (error) {
        console.log("Not authenticated");
        setLoading(false);
        setLoggedIn(false);
      }
    })();
  }, []);
  return (
    <div>
      <h1 className="center">Welcome to this React Application</h1>
      <hr></hr>
      {loading && <h2>Loading...</h2>}
      { loggedIn && 
        <div> 
          <h2 className="centerText ">You are Successfully Logged in</h2>

     
            {listItems}
            

         
          <Button
            className="button123 my-5"
            variant="outline-secondary"
            onClick={logoutUser}
          >
            Logout
          </Button>
        </div>
      }
      { !loading && !loggedIn &&
        <div>
          <h2 className="centerText">
            <h4>
              <strong>you are not logged in</strong>
            </h4>
          </h2>
          <Container>
            <Row className="mt-5">
              <Col md={{ span: 4, offset: 2 }}>
                <a href="/login">
                  {" "}
                  <Button variant="outline-primary">login</Button>
                </a>
              </Col>
              <Col md={3}>
                <a href="/register">
                  <Button variant="outline-secondary">Register</Button>
                </a>
              </Col>
            </Row>
          </Container>
        </div>
      } 
    </div>
  );
};

export default LandingPage;

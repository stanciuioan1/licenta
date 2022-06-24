import React, { useState, useEffect } from "react";
import "../index.css";
import { Container, Row, Col, Button } from "react-bootstrap";
import httpClient from "./httpClient";
import { User } from "../types";


const LandingPage = () => {
  const [user, setUser] = useState(User);
  const logoutUser = async () => {
    await httpClient.post("//localhost:5000/logout");
    window.location.href = "/";
  };

  function handleClick  (e){


    localStorage.setItem("problem_no",e);
    console.log("da" + e.toString())
  };
  const numbers = [1, 2, 3, 4, 5];
  const listItems = numbers.map((number) =>
  <h1 /*onClick={handleClick(number.toString())}*/><a href={`/problem?no=${number.toString()}`} /*key={number.toString()  }*/>
    {number}
  </a></h1>
);

  useEffect(() => {
    (async () => {
      try {
        const resp = await httpClient.get("//localhost:5000/user");

        console.log(resp.data)

        setUser(resp.data);

      } catch (error) {
        console.log("Not authenticated");
      }
    })();
  }, []);
  return (
    <div>
      <h1 className="center">Welcome to this React Application</h1>
      <hr></hr>
      {user != null ? (
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
      ) : (
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
      )}
    </div>
  );
};

export default LandingPage;

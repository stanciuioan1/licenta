import React, { useState, useEffect } from "react";
import "../index.css";
import { Container, Row, Col, Button } from "react-bootstrap";
import httpClient from "./httpClient";
import { User } from "../types";

const ProblemPage = () => {
  const [user, setUser] = useState(User);
  const [date_intrare, setDate_intrare] = useState("");
  const [date_iesire, setDate_iesire] = useState("");
  const [enunt, setEnunt] = useState("");
  const [exemplu, setExemplu] = useState("");

  const logoutUser = async () => {
    await httpClient.post("//localhost:5000/logout");
    window.location.href = "/";
  };

  function handleClick  (a){

    console.log(a);
    console.log("bucegi");
  };
  const numbers = [1, 2, 3, 4, 5];
  const listItems = numbers.map((number) =>
  <a href="/problem" onClick={handleClick(number.toString())} key={number.toString()  }>
    {number}
  </a>
);

const getProblem_no = ()=> sessionStorage.getItem("problem_no");
const [problem_no, setProblem_no] = useState(getProblem_no());

  useEffect(() => {
    (async () => {
      try {
        const data = getProblem_no();
        if(data) setProblem_no(data);
        const resp = await httpClient.get("//localhost:5000/user");
        const resp2 = await httpClient.get("//localhost:5000/enunt/" + problem_no.toString());
        const resp3 = await httpClient.get("//localhost:5000/date_intrare/" + problem_no.toString());
        const resp4 = await httpClient.get("//localhost:5000/date_iesire/" + problem_no.toString());
        const resp5 = await httpClient.get("//localhost:5000/exemplu/" + problem_no.toString());
        console.log(resp.data)

        setUser(resp.data);

        setEnunt(resp2.data);
        setDate_intrare(resp3.data);
        setDate_iesire(resp4.data);
        setExemplu(resp5.data);

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
          
            <h4 className="centerText pt-4">{enunt}</h4>
            <p></p>
            <h4 className="centerText pt-4">{date_intrare}</h4>
            <p></p>
            <h4 className="centerText pt-4">{enunt}</h4>
            <p></p>
            <h4 className="centerText pt-4">{exemplu}</h4>
            <p></p>
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

export default ProblemPage;

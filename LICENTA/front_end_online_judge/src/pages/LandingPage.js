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
  function range(start, end) {
    return Array(end - start + 1).fill().map((_, idx) => start + idx)
  }
  
  function convert_numbers_to_list(numbers){
    return numbers.map((number) =>
    <ul class = "unordered-list">
    <li class = "unordered-list"><a class = "dist" href={`/problem?no=${number.toString()}`}>
      {number}
    </a></li>
    </ul>
  );
  }

  
  const listItems1 = convert_numbers_to_list(range(1,20))
  const listItems2 = convert_numbers_to_list(range(21,40))
  const listItems3 = convert_numbers_to_list(range(41,60))
  const listItems4 = convert_numbers_to_list(range(61,80))
  const listItems5 = convert_numbers_to_list(range(81,100))
  const listItems6 = convert_numbers_to_list(range(101,120))
  const listItems7 = convert_numbers_to_list(range(121,140))
  const listItems8 = convert_numbers_to_list(range(141,160))
  const listItems9 = convert_numbers_to_list(range(161,180))
  const listItems10 = convert_numbers_to_list(range(181,200))
  const listItems11 = convert_numbers_to_list(range(201,220))
  const listItems12 = convert_numbers_to_list(range(221,240))
  const listItems13 = convert_numbers_to_list(range(241,260))
  const listItems14 = convert_numbers_to_list(range(261,280))
  const listItems15 = convert_numbers_to_list(range(281,300))
  const listItems16 = convert_numbers_to_list(range(301,320))
  const listItems17 = convert_numbers_to_list(range(321,340))
  const listItems18 = convert_numbers_to_list(range(341,360))
  const listItems19 = convert_numbers_to_list(range(361,380))
  const listItems20 = convert_numbers_to_list(range(381,400))
  const listItems21 = convert_numbers_to_list(range(401,420))
  const listItems22 = convert_numbers_to_list(range(421,440))
  const listItems23 = convert_numbers_to_list(range(441,460))
  const listItems24 = convert_numbers_to_list(range(461,479))




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
      <h1 className="center">Online Judge</h1>
      <hr></hr>
      {loading && <h2>Loading...</h2>}
      { loggedIn && 
        <div> 
          <h2 className="centerText ">You are Successfully Logged in</h2>

            <h1>Probleme arbori simple</h1>
            {listItems1}
            <br></br>
            <br></br>
            <br></br>
            <p><h1>Probleme arbori medii</h1></p>
            {listItems2}
            <br></br>
            <br></br>
            <br></br>
            <h1>Probleme arbori grele</h1>
            {listItems3}
            <br></br>
            <br></br>
            <br></br>
            <h1>Probleme grafuri simple</h1>
            {listItems4}
            <br></br>
            <br></br>
            <br></br>
            <p><h1>Probleme grafuri medii</h1></p>
            {listItems5}
            <br></br>
            <br></br>
            <br></br>
            <h1>Probleme grafuri grele</h1>
            {listItems6}
            <br></br>
            <br></br>
            <br></br>
            <h1>Probleme stiva simple</h1>
            {listItems7}
            <br></br>
            <br></br>
            <br></br>
            <p><h1>Probleme stiva medii</h1></p>
            {listItems8}
            <br></br>
            <br></br>
            <br></br>
            <h1>Probleme stiva grele</h1>
            {listItems9}
            <br></br>
            <br></br>
            <br></br>
            <h1>Probleme coada simple</h1>
            {listItems10}
            <br></br>
            <br></br>
            <br></br>
            <p><h1>Probleme coada medii</h1></p>
            {listItems11}
            <br></br>
            <br></br>
            <br></br>
            <h1>Probleme coada grele</h1>
            {listItems12}
            <br></br>
            <br></br>
            <br></br>
            <h1>Probleme programare dinamica simple</h1>
            {listItems13}
            <br></br>
            <br></br>
            <br></br>
            <p><h1>Probleme programare dinamica medii</h1></p>
            {listItems14}
            <br></br>
            <br></br>
            <br></br>
            <h1>Probleme programare dinamica grele</h1>
            {listItems15}
            <br></br>
            <br></br>
            <br></br>
            <h1>Probleme geometrie simple</h1>
            {listItems16}
            <br></br>
            <br></br>
            <br></br>
            <p><h1>Probleme geometrie medii</h1></p>
            {listItems17}
            <br></br>
            <br></br>
            <br></br>
            <h1>Probleme geometrie grele</h1>
            {listItems18}
            <br></br>
            <br></br>
            <br></br>
            <h1>Probleme hash simple</h1>
            {listItems19}
            <br></br>
            <br></br>
            <br></br>
            <p><h1>Probleme hash medii</h1></p>
            {listItems20}
            <br></br>
            <br></br>
            <br></br>
            <h1>Probleme hash grele</h1>
            {listItems21}
            <br></br>
            <br></br>
            <br></br>
            <h1>Probleme backtracking simple</h1>
            {listItems22}
            <br></br>
            <br></br>
            <br></br>
            <p><h1>Probleme backtracking medii</h1></p>
            {listItems23}
            <br></br>
            <br></br>
            <br></br>
            <h1>Probleme backtracking grele</h1>
            {listItems24}
            <br></br>
            <br></br>
            <br></br>
            

         <br></br>
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

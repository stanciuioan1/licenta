import React, { useState, useEffect } from "react";
import "../index.css";
import { Container, Row, Col, Button } from "react-bootstrap";
import httpClient from "./httpClient";
import { User } from "../types";
import AceEditor from 'react-ace'
import { useLocation } from 'react-router-dom';
import  queryString, { stringify } from 'query-string';
import { encode as base64_encode} from 'base-64';

import 'ace-builds/src-noconflict/mode-javascript'
// there are many themes to import, I liked monokai.
import 'ace-builds/src-noconflict/theme-monokai'
import 'ace-builds/src-noconflict/ext-language_tools'
import 'ace-builds/src-noconflict/ext-beautify'



const ProblemPage = () => {
  const [loading, setLoading] = useState(true);
  const [loggedIn, setLoggedIn] = useState(false);
  const [user, setUser] = useState(User);
  const [date_intrare, setDate_intrare] = useState("");
  const [date_iesire, setDate_iesire] = useState("");
  const [enunt, setEnunt] = useState("");
  const [exemplu, setExemplu] = useState("");
  const [scor1, setScor1] = useState("");
  const [scor2, setScor2] = useState("");
  const [scor3, setScor3] = useState("");
  const [scor4, setScor4] = useState("");
  const [rec_continut, setRec_continut] = useState("");
  const [rec_colab, setRec_colab] = useState("");

  const [code1, setCode1] = useState(`#include <iostream>

  using namespace std;
  
  
  int main()
  {
      
      return 0;
  }`)
  
  const location = useLocation();
  console.log(location);
  const parsed = queryString.parse(location.search);
  console.log(parsed);    
  const compileCode = async () => {
    
    let code = base64_encode(code1);
    //await httpClient.post("//localhost:5000/logout");
    //window.location.href = "/";

    let req = {
        "code" : code
    };

    let response = await httpClient.post("http://localhost:5000/compile/"+ parsed.no.toString(), req);
    
    console.log(response.data)
    if (response.data.tests["1"] === true)
    setScor1("correct")
    else
    if (response.data.tests["1"] == 'ec')
    setScor1("compile error")
    else
    if (response.data.tests["1"] == 408)
    setScor1("time limit exceeded")
    else
    setScor1("wrong answer");


    if (response.data.tests["2"] === true)
    setScor2("correct")
    else
    if (response.data.tests["2"] == 'ec')
    setScor2("compile error")
    else
    if (response.data.tests["2"] == 408)
    setScor2("time limit exceeded")
    else
    setScor2("wrong answer");

    if (response.data.tests["3"] === true)
    setScor3("correct")
    else
    if (response.data.tests["3"] == 'ec')
    setScor3("compile error")
    else
    if (response.data.tests["3"] == 408)
    setScor3("time limit exceeded")
    else
    setScor3("wrong answer");

    if (response.data.tests["4"] === true)
    setScor4("correct")
    else
    if (response.data.tests["4"] == 'ec')
    setScor4("compile error")
    else
    if (response.data.tests["4"] == 408)
    setScor4("time limit exceeded")
    else
    setScor4("wrong answer");


    console.log(response.data.tests)
  };

  const logoutUser = async () => {
    await httpClient.post("//localhost:5000/logout");
    window.location.href = "/";
  };



const getProblem_no = ()=> localStorage.getItem("problem_no");
const [problem_no, setProblem_no] = useState(getProblem_no());

  useEffect(() => {
    (async () => {
      try {
        const data = getProblem_no();
       
        if(data) setProblem_no(data);
        const resp = await httpClient.get("//localhost:5000/user");
        const resp2 = await httpClient.get("//localhost:5000/enunt/" + parsed.no.toString());
        const resp3 = await httpClient.get("//localhost:5000/date_intrare/" + parsed.no.toString());
        const resp4 = await httpClient.get("//localhost:5000/date_iesire/" + parsed.no.toString());
        const resp5 = await httpClient.get("//localhost:5000/exemplu/" + parsed.no.toString());
        const resp6 = await httpClient.get("//localhost:5000/get_content_based_recommendation/" + parsed.no.toString());
        const resp7 = await httpClient.get("//localhost:5000/get_my_collaborative_recommendation/" + parsed.no.toString());
        console.log(resp.data)

        setUser(resp.data);

        setEnunt(resp2.data);
        setDate_intrare(resp3.data);
        setDate_iesire(resp4.data);
        setExemplu(resp5.data);
        setRec_continut(resp6.data.msg);
        setRec_colab(resp7.data.msg);

        console.log(resp6.data.msg);
        console.log(resp7.data.msg);
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
      <h1 className="center">Online judge</h1>
      <hr></hr>
      {loading && <h2>Loading...</h2>}
      { loggedIn && 
        <div> 
          
            <h4 className="centerText pt-4">{enunt}</h4>
            <p></p>
            <h4 className="centerText pt-4">{date_intrare}</h4>
            <p></p>
            <h4 className="centerText pt-4">{date_iesire}</h4>
            <p></p>
            <h4 className="centerText pt-4">{exemplu}</h4>
            <p></p>

            <h1>Recomandam si: </h1>
            <ol >
                <li>{rec_continut[0]}</li>
                <li>{rec_continut[1]}</li>
                <li>{rec_continut[2]}</li>
                <li>{rec_continut[3]}</li>
                <li>{rec_continut[4]}</li>
            </ol>
            <br></br>
            <br></br>
            <br></br>
            <h1>Altii au rezolvat si: </h1>
            <ul >
                <li >{rec_colab[0]}</li>
                <li >{rec_colab[1]}</li>
                <li >{rec_colab[2]}</li>
                <li >{rec_colab[3]}</li>
                <li >{rec_colab[4]}</li>
            </ul>
            <Button
            className="button123 my-5"
            variant="outline-secondary"
            onClick={compileCode}
          >
            Compile
          </Button>
          <ol>
            <li>{scor1}</li>
            <li>{scor2}</li>
            <li>{scor3}</li>
            <li>{scor4}</li>
            </ol>
            <AceEditor 
            style={{
                height: '100vh',
                width: '100%',
            }}
            placeholder='Start Coding'
            theme='monokai'
            name='basic-code-editor'
            onChange={currentCode => setCode1(currentCode)}
            fontSize={18}
            showPrintMargin={true}
            showGutter={true}
            highlightActiveLine={true}
            value={code1}
            setOptions={{
                enableBasicAutocompletion: true,
                enableLiveAutocompletion: true,
                enableSnippets: true,
                showLineNumbers: true,
                tabSize: 4,
            }}
        />

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

export default ProblemPage;

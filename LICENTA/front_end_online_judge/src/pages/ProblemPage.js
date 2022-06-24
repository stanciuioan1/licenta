import React, { useState, useEffect } from "react";
import "../index.css";
import { Container, Row, Col, Button } from "react-bootstrap";
import httpClient from "./httpClient";
import { User } from "../types";
import AceEditor from 'react-ace'
import { useLocation } from 'react-router-dom';
import  queryString, { stringify } from 'query-string';
import {decode as base64_decode, encode as base64_encode} from 'base-64';

// import mode-<language> , this imports the style and colors for the selected language.
import 'ace-builds/src-noconflict/mode-javascript'
// there are many themes to import, I liked monokai.
import 'ace-builds/src-noconflict/theme-monokai'
// this is an optional import just improved the interaction.
import 'ace-builds/src-noconflict/ext-language_tools'
import 'ace-builds/src-noconflict/ext-beautify'



const ProblemPage = () => {
  const [user, setUser] = useState(User);
  const [date_intrare, setDate_intrare] = useState("");
  const [date_iesire, setDate_iesire] = useState("");
  const [enunt, setEnunt] = useState("");
  const [exemplu, setExemplu] = useState("");
  const [scor, setScor] = useState("");
  const [code1, setCode1] = useState(`function hello() {
    console.log("Hello World!");
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
    setScor(response.data.tests)
    //console.log(response)
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
            <h4 className="centerText pt-4">{date_iesire}</h4>
            <p></p>
            <h4 className="centerText pt-4">{exemplu}</h4>
            <p></p>
            <Button
            className="button123 my-5"
            variant="outline-secondary"
            onClick={compileCode}
          >
            Compile
          </Button>
          {scor}
            <AceEditor 
            style={{
                height: '100vh',
                width: '100%',
            }}
            placeholder='Start Coding'
            mode='javascript'
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

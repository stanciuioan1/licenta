import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import LandingPage from "./pages/LandingPage";
import Login from "./pages/Login";
import Registration from "./pages/Registration";
import NotFound from "./pages/NotFound";
import ProblemPage from "./pages/ProblemPage";

const Router = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" exact element={<LandingPage />} />
        <Route path="/login" exact element={<Login />} />
        <Route path="/register" exact element={<Registration />} />
        <Route path="/problem" exact element={<ProblemPage />} />
        <Route path="/*" exact element={<NotFound />} /> 
      </Routes>
    </BrowserRouter>
  );
};

export default Router;

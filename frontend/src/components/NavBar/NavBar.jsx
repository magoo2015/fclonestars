import React from "react";
import { useContext } from "react";
import { useNavigate, Link } from "react-router-dom";
import AuthContext from "../../context/AuthContext";
import "./NavBar.css";
// import logo from "../../images/fclonestar_logo.jpg";

const Navbar = () => {
  const { logoutUser, user } = useContext(AuthContext);
  const navigate = useNavigate();
  return (
    <div className="navBar">
      
      <ul>
        <li className="brand">
          <Link
            to="/"
            style={{ textDecoration: "none", color: "white" }}
          ><p>FCLONESTARS</p></Link>
        </li>


        <li>About</li>
        <li>Schedule</li>
        <li>Players</li>
        <li>
          {user ? (
            <button onClick={logoutUser}>Logout</button>
          ) : (
            <button onClick={() => navigate("/login")}>Login</button>
          )}
        </li>
      </ul>
    </div>
  );
};

export default Navbar;

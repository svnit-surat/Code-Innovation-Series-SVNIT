import React from "react";
import { withRouter } from "react-router-dom";
// import DarkToggle from "../components/darktoggle";

const NavBar = ({ history, user, logout }) => {
	const url = String(history.location.pathname);

	const logOut = () => {
		logout();
	};

	return (
		<div className="NavBar">
			<div className="logo">
				<div onClick={() => history.push("/")}>
					<h1>Pied Piper</h1>
				</div>
			</div>
			<div className="links">
				{user ? (
					<React.Fragment>
						<div
							className={
								url === "/dashboard" || url === "/dashboardDoc"
									? "link selected"
									: "link"
							}
							onClick={() => {history.push("/dashboard");}}>
							Dashboard
						</div>
						<div
							className={
								url === "/profile" ? "link selected" : "link"
							}
							onClick={() => {
								history.push("/profile");
							}}>
							Profile
						</div>
						<div className="link" onClick={() => logOut()}>
							Logout
						</div>
					</React.Fragment>
				) : (
					<React.Fragment>
						<div
							className={
								url === "/signup" ? "link selected" : "link"
							}
							onClick={() => history.push("/signup")}>
							Register
						</div>
						<div
							className={
								url === "/login" ? "link selected" : "link"
							}
							onClick={() => history.push("/login")}>
							Login
						</div>
					</React.Fragment>
				)}
			</div>
			{/*<DarkToggle/>*/}
		</div>
	);
};

export default withRouter(NavBar);

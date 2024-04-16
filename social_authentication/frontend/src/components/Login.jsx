import { useEffect, useState } from "react";
import { Link, useNavigate, useSearchParams } from "react-router-dom";
import { toast } from "react-toastify";
import AxiosInstance from "../utils/AxiosInstance";
import ClipLoader from "react-spinners/ClipLoader";

const Login = () => {
  const navigate = useNavigate();
  const [searchparams] = useSearchParams();
  const [loader, setLoader] = useState(false);
  const [logindata, setLogindata] = useState({
    email: "",
    password: "",
  });

  const handleOnchange = (e) => {
    setLogindata({ ...logindata, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (logindata) {
      try {
        setLoader(true);
        const res = await AxiosInstance.post("/auth/login/", logindata);
        const response = res.data;
        const user = {
          full_name: response.full_name,
          email: response.email,
        };

        if (res.status === 200) {
          localStorage.setItem("access", JSON.stringify(response.access_token));
          localStorage.setItem(
            "refresh",
            JSON.stringify(response.refresh_token)
          );
          localStorage.setItem("user", JSON.stringify(user));
          await navigate("/dashboard");
          toast.success("login successful");
        } else {
          toast.error("something went wrong");
        }
      } catch (error) {
        toast.error("something went wrong");
      } finally {
        setLoader(false);
      }
    }
  };

  return (
    <div>
      <div className="form-container">
        <div style={{ width: "100%" }} className="wrapper">
          <h2>Login into your account</h2>
          <form action="" onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="">Email Address:</label>
              <input
                type="text"
                className="email-form"
                value={logindata.email}
                name="email"
                onChange={handleOnchange}
              />
            </div>

            <div className="form-group">
              <label htmlFor="">Password:</label>
              <input
                type="password"
                className="email-form"
                value={logindata.password}
                name="password"
                onChange={handleOnchange}
                
              />
            </div>

            {loader ? (
              <ClipLoader />
            ) : (
              <input type="submit" value="Submit" className="submitButton" />
            )}

            <p className="pass-link">
              <Link to={"/forget-password"}>forgot password</Link>
            </p>
          </form>
          
        </div>
      </div>
    </div>
  );
};

export default Login;

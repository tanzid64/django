import { useEffect, useState } from "react";
import axios from "axios";
import { toast } from "react-toastify";
import { useNavigate } from "react-router-dom";
import { ClipLoader } from "react-spinners";

const Signup = () => {
  const navigate = useNavigate();
  const [loader, setLoader] = useState(false);
  const [formdata, setFormdata] = useState({
    email: "",
    first_name: "",
    last_name: "",
    password: "",
    password2: "",
  });
  // const [error, setError] = useState("");

  const handleOnchange = (e) => {
    setFormdata({ ...formdata, [e.target.name]: e.target.value });
  };

  const handleSigninWithGoogle = async (response) => {
    const payload = response.credential;
    const server_res = await axios.post(
      "http://localhost:8000/api/v1/auth/google/",
      { access_token: payload }
    );
    const user = {
      full_name: server_res.data.full_name,
      email: server_res.data.email,
    };

    if (server_res.status === 200) {
      localStorage.setItem(
        "access",
        JSON.stringify(server_res.data.access_token)
      );
      localStorage.setItem(
        "refresh",
        JSON.stringify(server_res.data.refresh_token)
      );
      localStorage.setItem("user", JSON.stringify(user));
      await navigate("/dashboard");
      toast.success("login successful");
    }
  };
  useEffect(() => {
    /* global google */
    google.accounts.id.initialize({
      client_id: import.meta.env.VITE_GOOGLE_CLIENT_ID,
      callback: handleSigninWithGoogle,
    });
    google.accounts.id.renderButton(document.getElementById("signInDiv"), {
      theme: "outline",
      size: "large",
      text: "continue_with",
      shape: "circle",
      width: "280",
    });
  }, []);

  const { email, first_name, last_name, password, password2 } = formdata;

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      setLoader(true)
      const response = await axios.post(
        "http://localhost:8000/api/v1/auth/register/",
        formdata
      );

      const result = response.data;
      if (response.status === 201) {
        navigate("/otp/verify");
        toast.success(result.message);
      }
    } catch (error) {
      toast.error("something went wrong");
    } finally{
      setLoader(false)
    }
  };

  return (
    <div>
      <div className="form-container">
        <div style={{ width: "100%" }} className="wrapper">
          <h2>create account</h2>
          <form action="" onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="">Email Address:</label>
              <input
                type="text"
                className="email-form"
                name="email"
                value={email}
                onChange={handleOnchange}
              />
            </div>
            <div className="form-group">
              <label htmlFor="">First Name:</label>
              <input
                type="text"
                className="email-form"
                name="first_name"
                value={first_name}
                onChange={handleOnchange}
              />
            </div>
            <div className="form-group">
              <label htmlFor="">Last Name:</label>
              <input
                type="text"
                className="email-form"
                name="last_name"
                value={last_name}
                onChange={handleOnchange}
              />
            </div>
            <div className="form-group">
              <label htmlFor="">Password:</label>
              <input
                type="text"
                className="email-form"
                name="password"
                value={password}
                onChange={handleOnchange}
              />
            </div>
            <div className="form-group">
              <label htmlFor="">Confirm Password:</label>
              <input
                type="text"
                className="p"
                name="password2"
                value={password2}
                onChange={handleOnchange}
              />
            </div>
            {loader ? (
              <ClipLoader />
            ) : (
              <input type="submit" value="Submit" className="submitButton" />
            )}
          </form>
          <h3 className="text-option">Or</h3>
          <div className="googleContainer">
            <div id="signInDiv" className="gsignIn"></div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Signup;

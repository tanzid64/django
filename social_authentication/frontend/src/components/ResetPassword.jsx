import { useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { toast } from "react-toastify";
import AxiosInstance from "../utils/AxiosInstance";
import axios from "axios";

const ResetPassword = () => {
  const navigate = useNavigate();
  const { uid, token } = useParams();
  const [newpasswords, setNewPassword] = useState({
    password: "",
    confirm_password: "",
  });
  const { password, confirm_password } = newpasswords;

  const handleChange = (e) => {
    setNewPassword({ ...newpasswords, [e.target.name]: e.target.value });
  };

  const data = {
    password: password,
    password2: confirm_password,
    uidb64: uid,
    token: token,
  };
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (data) {
      const res = await axios.patch(
        "http://127.0.0.1:8000/api/v1/auth/set-new-password/",
        data
      );
      console.log(res);
      const response = res.data;
      if (res.status === 200) {
        navigate("/login");
        toast.success(response.message);
      }
    }
  };
  return (
    <div>
      <div className="form-container">
        <div className="wrapper" style={{ width: "100%" }}>
          <h2>Enter your New Password</h2>
          <form action="" onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="">New Password:</label>
              <input
                type="password"
                className="email-form"
                name="password"
                value={password}
                onChange={handleChange}
              />
            </div>
            <div className="form-group">
              <label htmlFor="">Confirm Password</label>
              <input
                type="password"
                className="email-form"
                name="confirm_password"
                value={confirm_password}
                onChange={handleChange}
              />
            </div>
            <button type="submit" className="vbtn">
              Submit
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default ResetPassword;

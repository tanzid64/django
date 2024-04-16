import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axiosInstance from "../utils/AxiosInstance";
import { toast } from "react-toastify";

const Profile = () => {
  const navigate = useNavigate();
  const user = JSON.parse(localStorage.getItem("user"));
  const jwt_access = JSON.parse(localStorage.getItem("access"));
  console.log(jwt_access);
  useEffect(() => {
    if (jwt_access === null && !user) {
      navigate("/login");
    }
  }, [jwt_access, user]);
  const refresh = JSON.parse(localStorage.getItem("refresh"));
  console.log(refresh);
  const handleLogout = async () => {
    const res = await axiosInstance.post(
      "/auth/logout/",
      { "refresh_token": refresh }
    );
    console.log(res);
    if (res.status === 200) {
      localStorage.removeItem("refresh");
      localStorage.removeItem("access");
      localStorage.removeItem("user");
      navigate("/login");
      toast.success("Logout successfull");
    }
  };
  return (
    <div className="container">
      <h2>hi {user && user.full_name}</h2>
      <p style={{ textAlign: "center" }}>Welcome to your profile</p>
      <button onClick={handleLogout} className="logout-btn">
        Logout
      </button>
    </div>
  );
};

export default Profile;

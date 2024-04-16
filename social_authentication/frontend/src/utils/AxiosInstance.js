import axios from "axios";
import { jwtDecode } from "jwt-decode";
import dayjs from "dayjs";

const access_token = localStorage.getItem("access")
  ? JSON.parse(localStorage.getItem("access"))
  : "";
const refresh_token = localStorage.getItem("refresh")
  ? JSON.parse(localStorage.getItem("refresh"))
  : "";

const baseUrl = "http://localhost:8000/api/v1";
const axiosInstance = axios.create({
  baseURL: baseUrl,
  "content-type": "application/json",
  headers: {
    Authorization: localStorage.getItem("access")
      ? `Bearer ${access_token}`
      : null,
  },
});

// Checking access token is expired or not, if expired generate new from refresh and use new one.
axiosInstance.interceptors.request.use(async (req) => {
  if (access_token) {
    req.headers.Authorization = `Bearer ${access_token}`;
    const user = jwtDecode(access_token);
    const isExpired = dayjs.unix(user.exp).diff(dayjs()) < 1;
    if (!isExpired) {
      return req;
    } else {
      const res = await axios.post(`${baseUrl}/auth/token/refresh/`, {
        refresh: refresh_token,
      });
      if (res.status === 200) {
        localStorage.setItem("access", JSON.stringify(res.data.access));
        req.headers.Authorization = `Bearer ${res.data.access}`;
        return req;
      } else {
        localStorage.removeItem("refresh");
        localStorage.removeItem("access");
        localStorage.removeItem("user");
      }
    }
  }
  return req;
});

export default axiosInstance;

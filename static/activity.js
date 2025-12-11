// static/activity.js

function increaseActivity() {
  let count = parseInt(localStorage.getItem("exercises") || "0");
  count++;
  localStorage.setItem("exercises", count);
  localStorage.setItem("lastActive", new Date().toISOString());
}

function getActivity() {
  return parseInt(localStorage.getItem("exercises") || "0");
}

function getLastActive() {
  return localStorage.getItem("lastActive") || "Never";
}

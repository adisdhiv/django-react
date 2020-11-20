import http from "./http-common";

const getAll = () => {
  return http.get("/candidate-list/");
};

const get = id => {
  return http.get(`/candidate-detail/${id}`);
};

const create = data => {
  return http.post("/candidate-create/", data);
};

const update = (id, data) => {
  return http.put(`/candidate-update/${id}`, data);
};

const remove = id => {
  return http.delete(`/candidate-delete/${id}`);
};

export default {
  getAll,
  get,
  create,
  update,
  remove,
};
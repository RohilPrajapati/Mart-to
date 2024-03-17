import { SET_USER_DATA, SET_USER_TOKEN } from "./mutations";

export function storetoken({ commit }, data) {
  // console.log("aaaa")
  commit("SET_USER_TOKEN", data);
}

export function storeuser({ commit }, data) {
  commit("SET_USER_DATA", data);
}
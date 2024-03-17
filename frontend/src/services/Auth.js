import { loginUser } from "../pages/user/api/calls";
import { Store } from "../store/index";
class Auth {
  attempt(credentials) {
    return loginUser(credentials)
      .then(({ data }) => {
        Store.dispatch("user/storetoken", data);
        return this.getPayload(data.access);
      })
      .catch(error => {
        const data = {};
        Store.dispatch("user/storetoken", data);
        return Promise.reject(error);
      });
  }

  // postrefreshToken() {
  //   const refresh_token={
  //     "refresh":Store.state.user.auth.refresh
  //   };
  //   return refreshAccessToken(refresh_token)
  //     .then(({ data }) => {
  //       data.refresh = Store.state.user.auth.refresh
  //       Store.dispatch('user/storetoken', data)
  //       return this.getPayload(data.access);
  //     })
  //     .catch((error) => {
  //       const data = {}
  //       Store.dispatch('user/storetoken', data)
  //       return Promise.reject(error);
  //     });
  // }

  getPayload(token) {
    try {
      return JSON.parse(atob(token.split(".")[1]));
    } catch (e) {
      return null;
    }
  }

  check() {
    const payload = this.getPayload(Store.state.user.auth.access);
    return !!(payload && payload.user_id);
  }

  logout() {
    const data = {};
    Store.dispatch("user/storetoken", data);
  }
}

export default new Auth();

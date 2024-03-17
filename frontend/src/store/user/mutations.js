import user from ".";

export function SET_USER_TOKEN(state, data) {
    // console.log("aduaufyu")
    state.auth = data;
}

export function SET_USER_DATA(state, { ...data }) {
    state.user = data;
}
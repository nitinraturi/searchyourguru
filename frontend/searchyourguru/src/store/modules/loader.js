const state = {
  loading: false
}

const mutations = {
  setLoading(state, bool) {
    state.loading = bool
  }
}

const getters = {
  getLoading: state => {
    return state.loading
  }
}

export default {
  state,
  getters,
  mutations
}

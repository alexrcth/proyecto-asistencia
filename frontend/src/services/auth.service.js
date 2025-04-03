import api from './api';

export default {
  async login(username, password) {
    try {
      const response = await api.post('token/', { username, password });
      if (response.data.access) {
        localStorage.setItem('token', response.data.access);
        localStorage.setItem('refresh', response.data.refresh);
        return true;
      }
      return false;
    } catch (error) {
      console.error('Error during login:', error);
      return false;
    }
  },

  logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('refresh');
  },

  async register(username, email, password) {
    try {
      await api.post('register/', { username, email, password });
      return true;
    } catch (error) {
      console.error('Error during registration:', error);
      return false;
    }
  },

  async getCurrentUser() {
    try {
      const response = await api.get('users/me/');
      return response.data;
    } catch (error) {
      console.error('Error getting current user:', error);
      return null;
    }
  }
};
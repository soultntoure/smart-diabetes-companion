import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000'; // Default to local development

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  }
});

// Example API call for fetching user data
export const getUserData = async (userId) => {
  try {
    const response = await apiClient.get(`/users/${userId}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching user data:", error);
    throw error;
  }
};

// Example API call for logging glucose reading
export const logGlucoseReading = async (data) => {
  try {
    const response = await apiClient.post('/log/glucose', data);
    return response.data;
  } catch (error) {
    console.error("Error logging glucose reading:", error);
    throw error;
  }
};

// Add more API service functions as needed...

export default apiClient;

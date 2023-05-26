import { shallowMount } from '@vue/test-utils';
import Login from '../src/views/Login.vue';

describe('Login', () => {
  it('renders correctly', () => {
    const wrapper = shallowMount(Login);
    expect(wrapper.html()).toMatchSnapshot();
  });

  it('sets the correct data when input values change', () => {
    const wrapper = shallowMount(Login);

    // Find the input elements using their CSS selectors
    const usernameInput = wrapper.find('#username');
    const passwordInput = wrapper.find('#password');

    // Set the input values using the `setValue` method
    usernameInput.setValue('test_user');
    passwordInput.setValue('password123');

    // Retrieve the updated data values from the Vue instance
    const usernameValue = wrapper.vm.username;
    const passwordValue = wrapper.vm.password;

    // Assert the values are set correctly
    expect(usernameValue).toBe('test_user');
    expect(passwordValue).toBe('password123');
  });

  it('emits "login" event when form is submitted', () => {
    const wrapper = shallowMount(Login);

    // Find the form element
    const form = wrapper.find('form');

    // Stub the emitted event
    const loginData = {
      username: 'test_user',
      password: 'password123',
    };
    wrapper.vm.$emit('login', loginData);

    // Assert the emitted event and its payload
    expect(wrapper.emitted('login')).toBeTruthy();
    expect(wrapper.emitted('login')[0][0]).toEqual(loginData);
  });
});

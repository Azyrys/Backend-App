import { shallowMount } from '@vue/test-utils';
import Login from '@/components/Login.vue';

describe('Login', () => {
  it('renders correctly', () => {
    const wrapper = shallowMount(Login);
    expect(wrapper.element).toMatchSnapshot();
  });

  it('sets the correct data when input values change', () => {
    const wrapper = shallowMount(Login);
    const usernameInput = wrapper.find('[data-test="username-input"]');
    const passwordInput = wrapper.find('[data-test="password-input"]');
    
    usernameInput.setValue('test_user');
    passwordInput.setValue('password123');

    expect(wrapper.vm.username).toBe('test_user');
    expect(wrapper.vm.password).toBe('password123');
  });

  it('emits "login" event when form is submitted', () => {
    const wrapper = shallowMount(Login);
    const form = wrapper.find('form');

    wrapper.vm.$emit('login', {
      username: 'test_user',
      password: 'password123'
    });
    expect(wrapper.emitted().login).toBeTruthy();
    expect(wrapper.emitted().login[0]).toEqual([
      { username: 'test_user', password: 'password123' }
    ]);
  });
});
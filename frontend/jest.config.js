module.exports = {
    // ... other Jest configurations
    transform: {
      '^.+\\.vue$': 'vue-jest',
      '^.+\\.js$': 'babel-jest',
    },
    moduleFileExtensions: ['vue', 'js'],
    moduleNameMapper: {
      '^@/(.*)$': '<rootDir>/src/$1',
    },
  };

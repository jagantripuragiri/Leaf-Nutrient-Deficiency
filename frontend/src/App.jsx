import React, { useState } from 'react';
import styled from 'styled-components';
import { GlobalStyles } from './styles/GlobalStyles';
import Upload from './components/Upload';
import Result from './components/Result';

const AppContainer = styled.div`
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
`;

const Header = styled.header`
  text-align: center;
  margin-bottom: 3rem;
  
  h2 {
    font-size: 2.2rem;
    color: var(--primary);
    margin-bottom: 0.5rem;
    max-width: 800px;
    line-height: 1.3;
  }
  
  p {
    font-size: 1.1rem;
    color: var(--secondary);
  }
`;

function App() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const reset = () => setResult(null);

  return (
    <>
      <GlobalStyles />
      <AppContainer>
        <Header>
          <h2>Deep-Learning Based Detection of Nutrient
            Deficiency in Coffee plants using Leaf
            Analysis</h2>
          <p>Detect nutrient deficiencies and get organic remedies instantly.</p>
        </Header>

        {!result ? (
          <Upload setResult={setResult} setLoading={setLoading} loading={loading} />
        ) : (
          <Result result={result} reset={reset} />
        )}
      </AppContainer>
    </>
  );
}

export default App;

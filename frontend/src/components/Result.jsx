import React from 'react';
import styled from 'styled-components';
import { FaCheckCircle, FaExclamationTriangle } from 'react-icons/fa';

const ResultCard = styled.div`
  background: var(--white);
  padding: 2rem;
  border-radius: 20px;
  box-shadow: var(--shadow);
  width: 100%;
  max-width: 800px;
  display: flex;
  flex-direction: column;
  align-items: center;
`;

const ImagePreview = styled.img`
  width: 100%;
  max-width: 300px;
  border-radius: 15px;
  margin-bottom: 2rem;
  box-shadow: 0 4px 10px rgba(0,0,0,0.1);
`;

const Title = styled.h2`
  font-size: 2rem;
  color: ${props => props.isHealthy ? 'var(--primary)' : '#e76f51'};
  margin-bottom: 0.5rem;
  display: flex;
  align-items: center;
  gap: 10px;
`;

const Confidence = styled.p`
  color: #6c757d;
  font-size: 1rem;
  margin-bottom: 2rem;
`;

const Section = styled.div`
  width: 100%;
  text-align: left;
  margin-top: 1rem;
`;

const SectionTitle = styled.h3`
  color: var(--primary);
  border-bottom: 2px solid var(--secondary);
  padding-bottom: 0.5rem;
  margin-bottom: 1rem;
`;

const List = styled.ul`
  list-style-type: none;
`;

const ListItem = styled.li`
  background: #f0f7f4;
  margin-bottom: 0.5rem;
  padding: 1rem;
  border-radius: 10px;
  border-left: 5px solid var(--accent);
  font-size: 1.1rem;
`;

const BackButton = styled.button`
  margin-top: 2rem;
  padding: 10px 30px;
  background: var(--primary);
  color: white;
  font-size: 1rem;
  border-radius: 50px;
  
  &:hover {
    background: var(--secondary);
  }
`;

function Result({ result, reset }) {
    const isHealthy = result.deficiency.toLowerCase().includes('healthy');

    return (
        <ResultCard>
            <ImagePreview src={result.previewUrl} alt="Analyzed Leaf" />

            <Title isHealthy={isHealthy}>
                {isHealthy ? <FaCheckCircle /> : <FaExclamationTriangle />}
                {result.deficiency.replace('-', ' ')}
            </Title>

            <Confidence>Confidence: {result.confidence}</Confidence>

            <Section>
                <SectionTitle>Organic Remedies</SectionTitle>
                <List>
                    {result.organic_remedy.map((remedy, index) => (
                        <ListItem key={index}>{remedy}</ListItem>
                    ))}
                </List>
            </Section>

            <BackButton onClick={reset}>Analyze Another</BackButton>
        </ResultCard>
    );
}

export default Result;

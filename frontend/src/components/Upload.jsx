import React, { useState } from 'react';
import styled from 'styled-components';
import axios from 'axios';
import { FaCloudUploadAlt, FaSpinner } from 'react-icons/fa';

const UploadCard = styled.div`
  background: var(--glass);
  padding: 3rem;
  border-radius: 20px;
  box-shadow: var(--shadow);
  backdrop-filter: blur(10px);
  width: 100%;
  max_width: 600px;
  text-align: center;
  border: 2px dashed var(--secondary);
  transition: all 0.3s ease;

  &:hover {
    border-color: var(--primary);
    transform: translateY(-5px);
  }
`;

const HiddenInput = styled.input`
  display: none;
`;

const UploadLabel = styled.label`
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
  
  svg {
    font-size: 4rem;
    color: var(--secondary);
    margin-bottom: 1rem;
    transition: color 0.3s;
  }

  &:hover svg {
    color: var(--primary);
  }
`;

const UploadText = styled.p`
  font-size: 1.2rem;
  color: var(--text);
  font-weight: 500;
`;

const Spinner = styled(FaSpinner)`
  animation: spin 1s linear infinite;
  font-size: 3rem;
  color: var(--primary);
  margin-top: 1rem;

  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }
`;

function Upload({ setResult, setLoading, loading }) {
    const handleFileChange = async (e) => {
        const file = e.target.files[0];
        if (!file) return;

        setLoading(true);
        const formData = new FormData();
        formData.append('file', file);

        try {
            // Assuming backend is on port 8000
            const response = await axios.post('http://localhost:8000/predict', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });

            // Add the image URL for preview (local object URL)
            const previewUrl = URL.createObjectURL(file);
            setResult({ ...response.data, previewUrl });
        } catch (error) {
            console.error("Error uploading file:", error);
            alert("Failed to analyze image. Ensure backend is running.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <UploadCard>
            {loading ? (
                <div>
                    <Spinner />
                    <UploadText>Analyzing Leaf...</UploadText>
                </div>
            ) : (
                <>
                    <HiddenInput type="file" id="leaf-upload" accept="image/*" onChange={handleFileChange} />
                    <UploadLabel htmlFor="leaf-upload">
                        <FaCloudUploadAlt />
                        <UploadText>Click to Upload Leaf Image</UploadText>
                    </UploadLabel>
                </>
            )}
        </UploadCard>
    );
}

export default Upload;

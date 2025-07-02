import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import ImageUploader from './ImageUploader';

function createFile(name, type) {
  return new File(['dummy content'], name, { type });
}

describe('ImageUploader', () => {
  test('renders input element', () => {
    render(<ImageUploader />);
    expect(screen.getByLabelText(/upload image/i)).toBeInTheDocument();
  });

  test('accepts and displays an image file', () => {
    render(<ImageUploader />);
    const input = screen.getByLabelText(/upload image/i);

    const file = createFile('test.png', 'image/png');
    fireEvent.change(input, { target: { files: [file] } });

    const img = screen.getByAltText(/uploaded preview/i);
    expect(img).toBeInTheDocument();
  });

  test('shows error on non-image file', () => {
    render(<ImageUploader />);
    const input = screen.getByLabelText(/upload image/i);

    const file = createFile('test.txt', 'text/plain');
    fireEvent.change(input, { target: { files: [file] } });

    expect(screen.getByRole('alert')).toHaveTextContent(/only image files are allowed/i);
    expect(screen.queryByAltText(/uploaded preview/i)).toBeNull();
  });

  test('replaces image when uploading new file', () => {
    render(<ImageUploader />);
    const input = screen.getByLabelText(/upload image/i);

    const file1 = createFile('cat.png', 'image/png');
    fireEvent.change(input, { target: { files: [file1] } });
    expect(screen.getByAltText(/uploaded preview/i).src).toContain('cat.png');

    const file2 = createFile('dog.jpg', 'image/jpeg');
    fireEvent.change(input, { target: { files: [file2] } });
    expect(screen.getByAltText(/uploaded preview/i).src).toContain('dog.jpg');
  });
});

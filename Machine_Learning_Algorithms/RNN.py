import numpy as np

class Softmax:
    def forward(self, x):
        exp_x = np.exp(x - np.max(x, axis=0, keepdims=True))
        return exp_x / np.sum(exp_x, axis=0, keepdims=True)

class SimpleRNN:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.Whh = np.random.randn(hidden_size, hidden_size) * 0.01
        self.Wxh = np.random.randn(hidden_size, input_size) * 0.01
        self.Why = np.random.randn(output_size, hidden_size) * 0.01
        self.bh = np.zeros((hidden_size, 1))
        self.by = np.zeros((output_size, 1))
        self.softmax = Softmax() # Add the softmax layer

    def forward(self, x, h_prev):
        """
        Forward pass for a single time step.

        Args:
            x (numpy.ndarray): Input at the current time step (input_size, 1).
            h_prev (numpy.ndarray): Hidden state from the previous time step (hidden_size, 1).

        Returns:
            tuple: (h_next, y_pred_before_softmax, y_pred_proba)
                   where h_next is the next hidden state,
                   y_pred_before_softmax is the output before softmax,
                   and y_pred_proba is the output after softmax (probabilities).
        """
        h_next = np.tanh(np.dot(self.Whh, h_prev) + np.dot(self.Wxh, x) + self.bh)
        y_pred_before_softmax = np.dot(self.Why, h_next) + self.by
        y_pred_proba = self.softmax.forward(y_pred_before_softmax)
        return h_next, y_pred_before_softmax, y_pred_proba

# Example Usage (sequence processing with softmax at the end)
if __name__ == '__main__':
    # Example sequence: 3 time steps, input size 4
    sequence = np.random.randn(3, 4, 1)
    input_size = 4
    hidden_size = 5
    output_size = 2

    rnn_model = SimpleRNN(input_size, hidden_size, output_size)
    hidden_state = np.zeros((hidden_size, 1))
    final_output_before_softmax = None
    final_output_probabilities = None

    print("Processing Sequence:")
    for t in range(sequence.shape[0]):
        input_t = sequence[t]
        hidden_state, output_t_before_softmax, output_t_proba = rnn_model.forward(input_t, hidden_state)
        print(f"Time Step {t+1}:")
        print("  Input:", input_t.flatten())
        print("  Hidden State:", hidden_state.flatten())
        print("  Output (before softmax):", output_t_before_softmax.flatten())
        print("  Output (probabilities):", output_t_proba.flatten())
        if t == sequence.shape[0] - 1:
            final_output_before_softmax = output_t_before_softmax
            final_output_probabilities = output_t_proba

    if final_output_probabilities is not None:
        predicted_class = np.argmax(final_output_probabilities)
        print("\nFinal Output (before softmax):", final_output_before_softmax.flatten())
        print("Final Output (probabilities):", final_output_probabilities.flatten())
        print("Predicted Class:", predicted_class)
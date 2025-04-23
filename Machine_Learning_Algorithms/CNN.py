import numpy as np

class Conv2D:
    def __init__(self, in_channels, out_channels, kernel_size, stride=1):
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.stride = stride
        self.weights = np.random.randn(out_channels, in_channels, kernel_size, kernel_size) * 0.01
        self.bias = np.zeros(out_channels)

    def forward(self, x):
        n_samples, n_channels, height, width = x.shape
        out_height = (height - self.kernel_size) // self.stride + 1
        out_width = (width - self.kernel_size) // self.stride + 1
        output = np.zeros((n_samples, self.out_channels, out_height, out_width))

        for i in range(out_height):
            for j in range(out_width):
                h_start = i * self.stride
                h_end = h_start + self.kernel_size
                w_start = j * self.stride
                w_end = w_start + self.kernel_size
                input_slice = x[:, :, h_start:h_end, w_start:w_end]

                # Perform convolution for all output channels at this spatial location
                for out_c in range(self.out_channels):
                    output[:, out_c, i, j] = np.sum(input_slice * self.weights[out_c, :, :, :], axis=(1, 2, 3)) + self.bias[out_c]
        return output

class MaxPooling2D:
    def __init__(self, pool_size, stride=None):
        self.pool_size = pool_size
        self.stride = stride if stride is not None else pool_size

    def forward(self, x):
        n_samples, n_channels, height, width = x.shape
        out_height = (height - self.pool_size) // self.stride + 1
        out_width = (width - self.pool_size) // self.stride + 1
        output = np.zeros((n_samples, n_channels, out_height, out_width))

        for i in range(out_height):
            for j in range(out_width):
                h_start = i * self.stride
                h_end = h_start + self.pool_size
                w_start = j * self.stride
                w_end = w_start + self.pool_size
                input_slice = x[:, :, h_start:h_end, w_start:w_end]
                output[:, :, i, j] = np.max(input_slice, axis=(2, 3))
        return output

class Flatten:
    def forward(self, x):
        return x.reshape(x.shape[0], -1)

class Dense:
    def __init__(self, in_features, out_features):
        self.weights = np.random.randn(in_features, out_features) * 0.01
        self.bias = np.zeros(out_features)

    def forward(self, x):
        return np.dot(x, self.weights) + self.bias

class ReLU:
    def forward(self, x):
        return np.maximum(0, x)

class Softmax:
    def forward(self, x):
        exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))
        return exp_x / np.sum(exp_x, axis=1, keepdims=True)

# Basic CNN Model
class SimpleCNN:
    def __init__(self, in_channels, n_classes):
        self.conv1 = Conv2D(in_channels, 32, 3)
        self.relu1 = ReLU()
        self.pool1 = MaxPooling2D(2)
        self.flatten = Flatten()
        self.dense1 = Dense(32 * 13 * 13, 100) # Corrected input size
        self.relu2 = ReLU()
        self.dense2 = Dense(100, n_classes)
        self.softmax = Softmax()

    def forward(self, x):
        x = self.pool1.forward(self.relu1.forward(self.conv1.forward(x)))
        x = self.flatten.forward(x)
        x = self.relu2.forward(self.dense1.forward(x))
        return self.softmax.forward(self.dense2.forward(x))

# Example Usage (dummy input)
if __name__ == '__main__':
    # Dummy input: 1 sample, 1 channel (grayscale), 28x28 image
    input_data = np.random.rand(1, 1, 28, 28)
    cnn_model = SimpleCNN(in_channels=1, n_classes=10)
    output = cnn_model.forward(input_data)
    print("CNN Output Shape:", output.shape)
    print("CNN Output (probabilities):", output)
import os.path as osp

from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

ROOT = osp.dirname(osp.abspath(__file__))

setup(
    name="lietorch",
    version="0.2",
    description="Lie Groups for PyTorch",
    author="teedrz",
    packages=["lietorch"],
    # install_requires=[
    #     "numpy",
    #     "scipy",
    #     "torch",
    #     "torchvision",
    # ],
    setup_requires=[
        "torch",
    ],
    ext_modules=[
        CUDAExtension(
            "lietorch_backends",
            include_dirs=[osp.join(ROOT, "lietorch/include"), osp.join(ROOT, "eigen")],
            sources=[
                "lietorch/src/lietorch.cpp",
                "lietorch/src/lietorch_gpu.cu",
                "lietorch/src/lietorch_cpu.cpp",
            ],
            extra_compile_args={
                "cxx": ["-O3"],
                "nvcc": [
                    "-O3",
                    # "-gencode=arch=compute_60,code=sm_60",  # Pascal: GTX 1080, 1070, etc.
                    # "-gencode=arch=compute_70,code=sm_70",  # Volta: V100
                    # "-gencode=arch=compute_75,code=sm_75",  # Turing: RTX 2080, etc.
                    "-gencode=arch=compute_80,code=sm_80",  # Ampere: A100, RTX 3090, etc.
                    "-gencode=arch=compute_86,code=sm_86",  # Ampere: RTX 3050, 3060, etc.
                    "-gencode=arch=compute_89,code=sm_89",  # Hopper: H100
                    # "-gencode=arch=compute_89,code=compute_89",  # PTX for future compatibility
                ],
            },
        ),
        CUDAExtension(
            "lietorch_extras",
            sources=[
                "lietorch/extras/altcorr_kernel.cu",
                "lietorch/extras/corr_index_kernel.cu",
                "lietorch/extras/se3_builder.cu",
                "lietorch/extras/se3_inplace_builder.cu",
                "lietorch/extras/se3_solver.cu",
                "lietorch/extras/extras.cpp",
            ],
            extra_compile_args={
                "cxx": ["-O3"],
                "nvcc": [
                    "-O3",
                    # "-gencode=arch=compute_60,code=sm_60",  # Pascal: GTX 1080, 1070, etc.
                    # "-gencode=arch=compute_70,code=sm_70",  # Volta: V100
                    # "-gencode=arch=compute_75,code=sm_75",  # Turing: RTX 2080, etc.
                    "-gencode=arch=compute_80,code=sm_80",  # Ampere: A100, RTX 3090, etc.
                    "-gencode=arch=compute_86,code=sm_86",  # Ampere: RTX 3050, 3060, etc.
                    "-gencode=arch=compute_89,code=sm_89",  # Hopper: H100
                    # "-gencode=arch=compute_89,code=compute_89",  # PTX for future compatibility
                ],
            },
        ),
    ],
    cmdclass={"build_ext": BuildExtension},
)

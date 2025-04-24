Alright, let's dive into the fascinating world of chemical elements and their neutrons to create an interesting problem!

**The Problem: The Isotopic Puzzle of Ancient Artifacts**

**Scenario:**

A team of archaeologists has unearthed several ancient artifacts from different historical periods. They've sent small samples of these artifacts for isotopic analysis to determine the age and origin of the materials. The analysis provides the relative abundance of different isotopes for a few key elements found in the artifacts.

You, a data scientist with a background in chemistry, have been tasked with analyzing this isotopic data to solve a puzzle: **Can you determine which artifact likely originated from the same source based on the neutron count variations in a specific element?**

**Detailed Information:**

1.  **Elements of Interest:** The analysis focused on the element **Tin (Sn)**, which has several stable isotopes.

2.  **Isotopic Data:** For each artifact, you have the relative abundance (as a percentage) of three specific isotopes of Tin:
    * Tin-118 ($^{118}$Sn): Contains 50 protons and 68 neutrons.
    * Tin-120 ($^{120}$Sn): Contains 50 protons and 70 neutrons.
    * Tin-122 ($^{122}$Sn): Contains 50 protons and 72 neutrons.

3.  **Artifact Data:** You have the following isotopic abundance data for Tin from four different artifacts:

    * **Artifact A:**
        * $^{118}$Sn: 24.1%
        * $^{120}$Sn: 32.6%
        * $^{122}$Sn: 4.8%

    * **Artifact B:**
        * $^{118}$Sn: 24.0%
        * $^{120}$Sn: 32.9%
        * $^{122}$Sn: 4.6%

    * **Artifact C:**
        * $^{118}$Sn: 10.5%
        * $^{120}$Sn: 15.2%
        * $^{122}$Sn: 25.8%

    * **Artifact D:**
        * $^{118}$Sn: 24.3%
        * $^{120}$Sn: 32.5%
        * $^{122}$Sn: 5.0%

4.  **The Underlying Principle:** Elements from the same geological source often have very similar isotopic ratios. Variations in these ratios can occur due to different geological processes or origins.

**The Task:**

Using one or more of the algorithms you've learned, determine which of the artifacts (if any) likely originated from the same source based on the similarity of their Tin isotopic abundance profiles. Describe the algorithm(s) you chose and why they are suitable for this problem. Explain your steps and the reasoning behind your conclusion.

**Think about:**

* How would you represent the isotopic data for each artifact?
* What metric or algorithm would best capture the similarity between these representations?
* How would you determine a threshold or criteria to decide if artifacts are "from the same source"?

This problem combines a bit of chemistry with data analysis, requiring you to apply algorithmic thinking to a real-world (or at least, plausible) scenario. Good luck solving the isotopic puzzle!
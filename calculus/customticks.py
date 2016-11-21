from fractions import Fraction
import numpy as np
def create_pi_labels(a, b, step):

    max_denominator = int(1/step)
    # i added this line and the .limit_denominator to solve an 
    # issue with floating point precision
    # because of floataing point precision Fraction(1/3) would be 
    # Fraction(6004799503160661, 18014398509481984)

    values = np.arange(a, b+step/10, step)
    fracs = [Fraction(x).limit_denominator(max_denominator) for x in values]
    ticks = values*np.pi

    labels = []

    for frac in fracs:
        if frac.numerator==0:
            labels.append(r"$0$")
        elif frac.numerator<0:
            if frac.denominator==1 and abs(frac.numerator)==1:
                labels.append(r"$-\pi$")
            elif frac.denominator==1:
                labels.append(r"$-{}\pi$".format(abs(frac.numerator)))
            else:
                labels.append(r"$-\frac{{{}}}{{{}}} \pi$".format(abs(frac.numerator), frac.denominator))
        else:
            if frac.denominator==1 and frac.numerator==1:
                labels.append(r"$\pi$")
            elif frac.denominator==1:
                labels.append(r"${}\pi$".format(frac.numerator))
            else:
                labels.append(r"$\frac{{{}}}{{{}}} \pi$".format(frac.numerator, frac.denominator))

    return ticks, labels

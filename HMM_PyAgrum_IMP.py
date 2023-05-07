# Import libraries
import cairosvg
import pyAgrum as gum
import pyAgrum.lib.notebook as gnb
import pyAgrum.lib.dynamicBN as gdyn
import matplotlib.pyplot as plt
# The main entry point for this module
def main():
    # Create a dynamic bayesian network
    model = gum.BayesNet()
    # Add umbrella nodes
    umbrella0 = gum.LabelizedVariable('Umbrella(0)','Umbrella day 0',2)
    umbrella0.changeLabel(0,'Yes')
    umbrella0.changeLabel(1,'No')
    u0 = model.add(umbrella0)
    umbrella1 = gum.LabelizedVariable('Umbrella(1)','Umbrella day 1',2)
    umbrella1.changeLabel(0,'Yes')
    umbrella1.changeLabel(1,'No')
    u1 = model.add(umbrella1)
    # Add weather nodes
    weather0 = gum.LabelizedVariable('Weather(0)','Weather day 0',2)
    weather0.changeLabel(0,'Sunny')
    weather0.changeLabel(1,'Rainy')
    w0 = model.add(weather0)
    weather1 = gum.LabelizedVariable('Weather(1)','Weather day 1',2)
    weather1.changeLabel(0,'Sunny')
    weather1.changeLabel(1,'Rainy')
    w1 = model.add(weather1)
    # Add connections between nodes (tail, head)
    model.addArc(u0, w0)
    model.addArc(w0, w1)
    model.addArc(u1, w1)
    # Visualize bayesian network
    svg = gnb.getBN(model)
    cairosvg.svg2png(bytestring=svg,write_to='plots\\dnb_chart.png')
    # Get time slices and save as image
    svg = gdyn.getTimeSlices(model)
    cairosvg.svg2png(bytestring=svg,write_to='plots\\dnb_time_slices.png')
    # Add CPT:s (Conditional probability tables)
    model.cpt(model.idFromName('Weather(0)'))[{'Umbrella(0)':'Yes'}]=[0.1, 0.8]
    model.cpt(model.idFromName('Weather(0)'))[{'Umbrella(0)':'No'}]=[0.9, 0.2]
    model.cpt(model.idFromName('Weather(1)'))[{'Umbrella(1)':'Yes'}]=[[0.25, 0.75], 
                                                                      [0.1, 0.9]]
    model.cpt(model.idFromName('Weather(1)'))[{'Umbrella(1)':'No'}]=[[0.9, 0.1], 
                                                                     [0.75, 0.25]]
    # Create an inference model
    ie = gum.LazyPropagation(model)
    # Make inference and print the results
    print('--- Umbrella(0): No ---')
    ie.setEvidence({'Umbrella(0)':'No'})
    ie.makeInference()
    print(ie.posterior('Weather(0)'))
    print()
    print('--- Umbrella(0): Yes ---')
    ie.setEvidence({'Umbrella(0)':'Yes'})
    ie.makeInference()
    print(ie.posterior('Weather(0)'))
    print()
    print('--- Weather(0): Sunny, Umbrella(1): Yes ---')
    ie.setEvidence({'Weather(0)':'Sunny', 'Umbrella(1)':'Yes'})
    ie.makeInference()
    #gnb.getPosterior(model, {'Weather(0)':'Sunny', 'Umbrella(1)':'Yes'}, 'Weather(1)')
    #plt.show()
    print(ie.posterior('Weather(1)'))
    print()
    print('--- Weather(0): Sunny, Umbrella(1): No ---')
    ie.setEvidence({'Weather(0)':'Sunny', 'Umbrella(1)':'No'})
    ie.makeInference()
    print(ie.posterior('Weather(1)'))
    print()
    print('--- Weather(0): Rainy, Umbrella(1): Yes ---')
    ie.setEvidence({'Weather(0)':'Rainy', 'Umbrella(1)':'Yes'})
    ie.makeInference()
    print(ie.posterior('Weather(1)'))
    print()
    print('--- Weather(0): Rainy, Umbrella(1): No ---')
    ie.setEvidence({'Weather(0)':'Rainy', 'Umbrella(1)':'No'})
    ie.makeInference()
    print(ie.posterior('Weather(1)'))
    print()
# Tell python to run main method
if __name__ == "__main__": main()

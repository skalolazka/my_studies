#!/usr/bin/perl

# task: determine if the letter l can be written using the given text from a magazine

use strict;
use warnings;

sub is_writable {
    my ($to_write, $base_text) = @_; # l - letter, m - magazine text
    #my @text = split(//, $m);
    my %symbols = (); # ok, here every symbol is counted as a letter, even whitespaces.
    # by the task I didn't understand if a whitespace is considered a letter or not,
    # here I do consider it a letter. If I shouldn't - tell me.
    for (split(//, $to_write)) {
        $symbols{$_}++;
    }
    for my $l (split(//, $base_text)) {
        if (defined($symbols{$l})) {
            if ($symbols{$l} > 1) {
                $symbols{$l}--;
            }
            else { # == 1
                delete($symbols{$l});
            }
        }
    }
    return scalar(keys(%symbols)) ? 0 : 1;
}

use Test::More;
use Test::Deep;

is(is_writable('', ''), 1, 'empty strings');
is(is_writable('a', ''), 0, 'one letter & none');
is(is_writable('a', 'a'), 1, 'one same letter');
is(is_writable('a', 'b'), 0, 'different letters');
is(is_writable('avt', 'sdfew'), 0, 'many different letters');
is(is_writable('aaaa', 'bbssaaaha'), 1, 'three same letters');
is(is_writable('bbbaabc', 'dddfbcababbt'), 1, 'long');
is(is_writable('a , 54 lsfddd --- lp', 'd shbcw4akdj--gvl, lddgsfd 5 - p  '), 1, 'long with spaces');

done_testing;
